// Load data
const rawData = JSON.parse(document.getElementById("pub-data").textContent);

// Normalize data
const publications = rawData.map(p => ({
    ...p,
    year: p.date ? new Date(p.date).getFullYear() : 'unknown',
    topics: (p.topic || []).map(t => t.display_label),
    authors: (p.author || []).map(a => `${a.given_name} ${a.family_name}`)
}));

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

    publications.forEach(p => {
        if (Array.isArray(p[field])) {
            p[field].forEach(v => values.add(v));
        } else if (p[field]) {
            values.add(p[field]);
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

// Render checkboxes for filters
function renderFilter(containerId, field, values) {
    const container = document.getElementById(containerId);
    values.forEach(value => {
        const id = `${field}-${value}`;
        const label = document.createElement("label");
        label.style.display = "block";
        const checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.value = value;
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
function matchesFilters(p) {
    // Kind
    if (state.kind.size && !state.kind.has(p.kind)) return false;
    // Year
    if (state.year.size && !state.year.has(String(p.year))) return false;
    // Topic (multi-value)
    if (state.topic.size) {
        const match = p.topics.some(t => state.topic.has(t));
        if (!match) return false;
    }
    return true;
}

// Search
function matchesSearch(p) {
    if (!state.search) return true;
    const text = (
        p.title +
        " " +
        p.kind +
        " " +
        p.topics.join(" ") +
        " " +
        p.authors.join(" ")
    ).toLowerCase();
    return text.includes(state.search);
}

// Render results
function render() {
    const container = document.getElementById("results");
    container.innerHTML = "";
    const filtered = publications.filter(p =>
        matchesFilters(p) && matchesSearch(p)
    );
    if (filtered.length === 0) {
        container.innerHTML = "<p>No results</p>";
        return;
    }
    filtered.forEach(p => {
        const div = document.createElement("div");
        div.className = "pub";
        div.innerHTML = `
      <h3><em>${p.title} ${p.year ? ' ('+p.year+')' : ''}</em></h3>
      <p><strong>Authors:</strong> ${p.authors.join(", ")}</p>
      <p><strong>Kind:</strong> ${formatValue("kind", p.kind)}</p>
      <p><strong>Topics:</strong> ${p.topics.join(", ")}</p>
    `;
        container.appendChild(div);
    });
}

// On startup:
// Build filters
renderFilter("filter-kind", "kind", getUniqueValues("kind"));
renderFilter("filter-topic", "topic", getUniqueValues("topics"));
renderFilter("filter-year", "year", getUniqueValues("year").map(String));
// Search input
document.getElementById("search").addEventListener("input", e => {
    state.search = e.target.value.toLowerCase();
    render();
});
// Initial render
render();