// js/app.js
const baseUrl = 'http://127.0.0.1:8000';


const getAppliances = async () => {
    const endpoint = `${baseUrl}/appliances`;
    const response = await fetch(endpoint);
    const appliances = await response.json();
    return appliances;
}

const getMinEnergy = async () => {
    const endpoint = `${baseUrl}/min/energy`;
    const response = await fetch(endpoint);
    const data = await response.json();
    return data;
}

const getOptimizedEnergy = async (totalEnergy) => {
    const endpoint = `${baseUrl}/optimized/consumption/${totalEnergy}`;
    const response = await fetch(endpoint);
    const data = await response.json();
    return data;
}

async function buildAppliancesTable(data) {
    const table = document.getElementById('appliance-table');
    table.innerHTML = '';
    const appliances = await data;
    appliances.forEach(appliance => {
        const row = document.createElement('tr');
        row.innerHTML = `
        <td>${appliance.name}</td>
        <td>${appliance.category}</td>
        <td>${appliance.power}</td>
        <td><button onclick="removeAppliance(${appliance.id})">Remove</button></td>
    `;
        row.id = appliance.id
        table.appendChild(row);
    });
}

async function updateMinEnergyLimit(minEnergy) {
    const input = document.getElementById('total-consumption');
    input.setAttribute('data-min', minEnergy);
    const warning_mess = document.getElementById('total-consumption-warning');
    // debugger;
    warning_mess.innerText = `Shall be superior to ${minEnergy / 1000.}kWh and inferior to 75kWh*`
}

async function renderMinEnergy() {
    try {
        const minEnergy = await getMinEnergy();
        updateMinEnergyLimit(minEnergy);
    } catch (error) {
        console.error('Error fetching and rendering minimum energy:', error);
    }

}

function validateTotalConsumption(input) {
    const maxValue = parseFloat(input.getAttribute('data-max'));
    const minValue = parseFloat(input.getAttribute('data-min'));
    const value = parseFloat(input.value);

    if ((value > maxValue) || (value < minValue)) {
        input.classList.add('invalid');
    } else {
        input.classList.remove('invalid');
    }
}

async function renderAppliances() {
    try {
        const data = await getAppliances();
        buildAppliancesTable(data);
    } catch (error) {
        console.error('Error fetching and rendering appliances:', error);
    }
}

async function deleteAppliance(applianceId) {
    const endpoint = `${baseUrl}/appliances/${applianceId}`;
    const content = {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    };
    try {
        const response = await fetch(endpoint, content);
        if (!response.ok) {
            throw new Error('Failed to delete appliance');
        }
        console.log(`Appliance with ID ${applianceId} deleted successfully`);
    } catch (error) {
        console.error('Error deleting appliance:', error);
        throw error;
    }
}

async function addAppliance() {
    const name = document.getElementById('appliance-name').value;
    const category = document.getElementById('appliance-category').value;
    const capacity = parseFloat(document.getElementById('appliance-capacity').value);
    const appliance = {
        "name": name,
        "category": category,
        "power": capacity
    };
    const endpoint = `${baseUrl}/appliances/`;
    const content = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(appliance)
    };
    try {
        const response = await fetch(endpoint, content);
        if (!response.ok) {
            throw new Error('Failed to create appliance');
        }
        console.log(`Appliance with ID ${response.appliance.id} added successfully`);
    } catch (error) {
        console.error('Error deleting appliance:', error);
        throw error;
    }
}

async function render() {
    await renderAppliances();
    await renderMinEnergy();

}
async function removeAppliance(applianceId) {
    await deleteAppliance(applianceId);
    await renderAppliances();
    await render();
}

async function createAppliance(applianceId) {
    await addAppliance(applianceId);
    await render();
}

async function renderTotalEnergyResults(energy_abs, energy_rel) {
    const resultsElt = document.getElementById('total-consumption-results');
    resultsElt.innerText = `The total consumption of energy is: ${energy_abs / 1000.}kWh (${(100*energy_rel).toFixed(2)}% of expected)`
}

async function renderEnergyByAppliance(appliances) {

    const labels = appliances.map(a => a.name);
    const consumptions = appliances.map(a => a.consumption);
    const times = appliances.map(a => a.duration)

    const ctxEnergy = document.getElementById('energyChart').getContext('2d');
    const ctxTime = document.getElementById('timeChart').getContext('2d');

    new Chart(ctxEnergy, {
        type: 'bar',
        data: {
            labels,
            datasets: [{
                label: 'Energy Consumption (Wh)',
                data: consumptions,
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
                data: times,
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

async function computeOpimal() {
    elt = document.getElementById('total-consumption');
    const totalEnergy = parseFloat(elt.value);
    const data = await getOptimizedEnergy(totalEnergy);
    const appliances = await data.appliances;
    const energy_abs = await data.total_energy_abs;
    const energy_rel = await data.total_energy_rel;
    renderTotalEnergyResults(energy_abs, energy_rel);
    renderEnergyByAppliance(appliances);
}