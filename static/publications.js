// Load data from all pre-rendered publication item divs
const publications = Array.from(document.querySelectorAll(".pub"));

// State
let state = {
    search: "",
    kind: new Set(),
    topic: new Set(),
    year: new Set()
};

// Build filter options dynamically
function getUniqueValues(field) {
    const values = new Set();
    publications.forEach(el => {
        if (field === "topic") {
            getTopics(el).forEach(v => values.add(v));
        } else {
            values.add(el.dataset[field]);
        }
    });
    return Array.from(values).sort();
}

// Format 'kind' display values
function formatValue(field, value) {
    if (value) {
        if (field == "kind") {
            return value.split(":").at(-1)
        }
    }
    return value
}

function renderFilter(containerId, field, values) {
    const container = document.getElementById(containerId);
    values.forEach(value => {
        const id = `${field}-${value}`;
        const label = document.createElement("label");
        label.style.display = "block";
        const checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.value = value;
        checkbox.dataset.field = field;
        checkbox.id = id;
        checkbox.addEventListener("change", () => {
            if (checkbox.checked) {
                state[field].add(value);
            } else {
                state[field].delete(value);
            }
            render();
        });
        label.appendChild(checkbox);
        label.appendChild(document.createTextNode(" " + formatValue(field, value)));
        container.appendChild(label);
    });
}

// Filtering logic
function matchesFilters(el) {
    const kind = el.dataset.kind;
    const year = el.dataset.year;
    const topics = getTopics(el);

    // kind filter
    if (state.kind.size && !state.kind.has(kind)) {
        return false;
    }
    // year filter
    if (state.year.size && !state.year.has(year)) {
        return false;
    }
    // topic filter (multi-match)
    if (state.topic.size) {
        const match = topics.some(t => state.topic.has(t));
        if (!match) return false;
    }
    return true;
}

// Helper to get topics from an element
function getTopics(el) {
    try {
        return JSON.parse(el.dataset.topics || "[]").map(t => t.display_label);
    } catch {
        return [];
    }
}

// Search logic
function matchesSearch(el) {
    if (!state.search) return true;
    const text = (
        el.dataset.title + " " +
        el.dataset.kind + " " +
        el.dataset.year + " " +
        el.dataset.topics + " " +
        el.dataset.authors
    ).toLowerCase();

    return text.includes(state.search);
}

// Change display of divs based on filtering/searching
function render() {
    let count = 0;
    publications.forEach(el => {
        const visible =
            matchesFilters(el) &&
            matchesSearch(el);
        if (visible) count+=1;
        renderCount(count)
        el.style.display = visible ? "" : "none";
    });
}

// Count of searched+filtered publications
function renderCount(count) {
    const countEl = document.getElementById('pub-count');
    countEl.innerHTML = `${count}` ;
}

// Set checkbox if user clicks on topic pill
function selectFilter(field, value) {
    const checkbox = document.querySelector(
        `input[type="checkbox"][data-field="${field}"][value="${CSS.escape(value)}"]`
    );
    if (!checkbox) return;
    if (!checkbox.checked) {
        checkbox.checked = true;
        state[field].add(value);
        render();
    }
}

// Clear all
function clearAllFilters() {
    // Reset state
    state.kind.clear();
    state.topic.clear();
    state.year.clear();
    state.search = "";
    // Uncheck all checkboxes
    document.querySelectorAll('input[type="checkbox"]').forEach(cb => {
        cb.checked = false;
    });
    // Clear search input
    const searchInput = document.getElementById("search");
    if (searchInput) {
        searchInput.value = "";
    }
    // Re-render results
    render();
}

// On startup:
// 1) Build filters
renderFilter("filter-kind", "kind", getUniqueValues("kind"));
renderFilter("filter-topic", "topic", getUniqueValues("topic"));
renderFilter("filter-year", "year", getUniqueValues("year").map(String));
// 2) Register search input
document.getElementById("search").addEventListener("input", e => {
    state.search = e.target.value.toLowerCase();
    render();
});
// 3) Add topic click handlers
document.querySelectorAll(".topic-chip").forEach(el => {
    el.addEventListener("click", () => {
        const topic = el.dataset.topic;
        selectFilter("topic", topic);
    });
});
// 4) Initial render
render();