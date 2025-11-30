const agentsGrid = document.querySelector('#agents-grid');

fetch('https://valorant-api.com/v1/agents')
    .then(res => res.json())
    .then(data => {
        const agents = data.data;
        console.log(agents);
        
        // dynamic rendering
        agents.forEach(agent => {
            agentsGrid.innerHTML += 
                `<div class="card">
                    <img src="${agent.fullPortrait}" alt="">
                    <h2>${agent.displayName}</h2>
                </div>
                `;
        });
    });