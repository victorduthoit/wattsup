// scripts.js

let appliances = [];

function addAppliance() {
    // Get input values
    const category = document.getElementById('appliance-category').value;
    const capacity = parseFloat(document.getElementById('appliance-capacity').value);

    // Add appliance to the list
    if (category && capacity > 0) {
        appliances.push({ category, capacity });
        renderAppliances();
        updateTotalConsumption();
    }
}

function renderAppliances() {
    const list = document.getElementById('appliance-list');
    list.innerHTML = '';

    appliances.forEach((appliance, index) => {
        const listItem = document.createElement('li');
        listItem.innerHTML = `${appliance.category} - ${appliance.capacity}W <button onclick="removeAppliance(${index})">Remove</button>`;
        list.appendChild(listItem);
    });
}

function removeAppliance(index) {
    appliances.splice(index, 1);
    renderAppliances();
    updateTotalConsumption();
}

function updateTotalConsumption() {
    const totalConsumption = appliances.reduce((total, appliance) => total + appliance.capacity, 0) / 1000; // Convert to kWh
    document.getElementById('total-consumption').textContent = totalConsumption.toFixed(2);
}

function launchOptimization() {
    alert('Optimization launched!');
    // Add optimization logic here
}

function startOver() {
    appliances = [];
    renderAppliances();
    updateTotalConsumption();
}
