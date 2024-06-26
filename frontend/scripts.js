// scripts.js

let appliances = [];

function addAppliance() {
    const name = document.getElementById('appliance-name').value;
    const category = document.getElementById('appliance-category').value;
    const capacity = parseFloat(document.getElementById('appliance-capacity').value);

    console.log(name, category, capacity)
    if (name && category && capacity > 0) {
        appliances.push({ name, category, capacity });
        renderAppliances();
    }
}

function renderAppliances() {
    const table = document.getElementById('appliance-table');
    table.innerHTML = '';

    appliances.forEach((appliance, index) => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${appliance.name}</td>
            <td>${appliance.category}</td>
            <td>${appliance.capacity}</td>
            <td><button onclick="removeAppliance(${index})">Remove</button></td>
        `;
        table.appendChild(row);
    });
}

function removeAppliance(index) {
    appliances.splice(index, 1);
    renderAppliances();
}

function validateTotalConsumption(input) {
    const maxValue = parseFloat(input.getAttribute('data-max')); // Get max value from data attribute
    const value = parseFloat(input.value);

    if (value > maxValue) {
        input.classList.add('invalid');
    } else {
        input.classList.remove('invalid');
    }
}

// Example usage in form
document.getElementById('inputCapacity').addEventListener('input', function () {
    validateInput(this);
});


function launchOptimization() {
    alert('Optimization launched!');
    // Add optimization logic here
}

function startOver() {
    appliances = [];
    updateTotalConsumption();
    updateCharts();
}

function updateCharts() {
    const labels = appliances.map(a => a.name);
    const capacities = appliances.map(a => a.capacity);

    const ctxEnergy = document.getElementById('energyChart').getContext('2d');
    const ctxTime = document.getElementById('timeChart').getContext('2d');

    new Chart(ctxEnergy, {
        type: 'bar',
        data: {
            labels,
            datasets: [{
                label: 'Energy Consumption (Wh)',
                data: capacities,
                backgroundColor: '#012160ff'
            }]
        },
        options: {
            scales: {
                x: { beginAtZero: true },
                y: { beginAtZero: true }
            }
        }
    });

    new Chart(ctxTime, {
        type: 'bar',
        data: {
            labels,
            datasets: [{
                label: 'Operating Time (h)',
                data: capacities.map(c => c / 100),
                backgroundColor: '#26d9c7ff'
            }]
        },
        options: {
            scales: {
                x: { beginAtZero: true },
                y: { beginAtZero: true }
            }
        }
    });
}

// Initialize empty charts
updateCharts();
