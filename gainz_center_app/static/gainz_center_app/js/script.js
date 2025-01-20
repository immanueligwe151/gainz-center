//used to collapse and expand faq divs
const faqQuestions = document.querySelectorAll('.collapsible-header');
faqQuestions.forEach((question) => {
    question.addEventListener('click', () => {
        // Get the respective collapsible-content and arrow inside the same collapsible-div
        const faqDiv = question.closest('.collapsible-div');
        const answer = faqDiv.querySelector('.collapsible-content');
        const arrow = faqDiv.querySelector('.arrow');
        
        // Check if the content is expanded or collapsed
        if (answer.style.maxHeight === "0px" || answer.style.maxHeight === "") {
            answer.style.maxHeight = answer.scrollHeight + "px"; // Expands answer
            arrow.style.transform = "rotate(180deg)"; // Rotates arrow up
        } else {
            answer.style.maxHeight = "0px"; // Collapses answer
            arrow.style.transform = "rotate(0deg)"; // Rotates arrow down
        }
    });
});

//used to open and close dialog boxes
window.addEventListener('click', function(event) {
    if (event.target === document.getElementById('dialog')) {
        closeDialog();
    }
});

function closeDialog() {
    document.getElementById('dialog').style.display = 'none';
};

function openDialog(input) {
    document.getElementById('dialog').style.display = 'flex';
    switch (input){
        case 1: //change password
            document.getElementById('change-password-div').style.display = 'block';
            document.getElementById('change-email-div').style.display = 'none';
            document.getElementById('delete-acc-div').style.display = 'none';   
        break;
        case 2: //change email
            document.getElementById('change-password-div').style.display = 'none';
            document.getElementById('change-email-div').style.display = 'block';
            document.getElementById('delete-acc-div').style.display = 'none'; 
        break;
        case 3: //delete account
            document.getElementById('change-password-div').style.display = 'none';
            document.getElementById('change-email-div').style.display = 'none';
            document.getElementById('delete-acc-div').style.display = 'block';
        break;
    }
}

//used for adding a new workout session
if (document.body.classList.contains('my-sessions-body')) { //if block is used to ensure that there are no parsing errors due to addEventListeners running when the elements aren't present in the DOM
    let workoutExercises = [];

    document.getElementById('add-exercise').addEventListener('click', () => {
        let exerciseName = document.getElementById('name-choice').value;
        let exerciseSet = document.getElementById('set-input').value;
        let exerciseRep = document.getElementById('reps-input').value;
        let exerciseWeight = document.getElementById('weight-input').value;
        let unit = document.getElementById('unit-input').value;

        let newExerciseHtml = "";
        let newExerciseObject = {};

        if (exerciseName == "" || exerciseSet == "" || exerciseRep == "" || exerciseWeight == "" || unit == "") {
            document.getElementById('missing-input').innerText = "You're missing at least one input. Please have a look and try again."
        } else {
            document.getElementById('missing-input').innerText = "";
            newExerciseHtml = `
            <tr class="basic-font">
                <td>${exerciseName}</td>
                <td>${exerciseSet}</td>
                <td>${exerciseRep}</td>
                <td>${exerciseWeight}${unit}</td>
            </tr>
        `
            document.getElementById('show-new-exercises').innerHTML += newExerciseHtml;

            newExerciseObject = {
                name: exerciseName,
                set: exerciseSet,
                rep: exerciseRep,
                weight: exerciseWeight,
                unit: unit,
            };

            workoutExercises.push(newExerciseObject);
        }
    });

    document.getElementById('new-session-btn').addEventListener('click', (event) => {
        event.preventDefault();
        let startTime = document.getElementById('start-time').value;
        let endTime = document.getElementById('end-time').value;
        if (startTime >= endTime) {
            document.getElementById('missing-input').innerText = "Can't start a workout before it's over; check your entered times!"
        } else if (workoutExercises.length == 0) {
            document.getElementById('missing-input').innerText = "You've not entered any exercises! Can't have a workout without one!"
        } else {
            document.getElementById('missing-input').innerText = "";

            const date = new Date(); // Get the current date
            const formattedStartTime = `${date.toISOString().split('T')[0]}T${startTime}:00`;
            const formattedEndTime = `${date.toISOString().split('T')[0]}T${endTime}:00`;
            const formattedCurrentDate = date.toISOString().split('T')[0];

            let newSession = {
                date: formattedCurrentDate,
                startTime: formattedStartTime,
                endTime: formattedEndTime,
                exercises: workoutExercises,
            }
            fetch('/add-new-session', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCsrfToken(),
                },
                body: JSON.stringify(newSession),
            })
                .then(response => response.json())
                .then(data => {
                    location.reload(); //refreshes the current page to show new entry
                })
                .catch(error => {
                    document.getElementById('missing-input').innerText = "There was a problem adding your session, please try again"
                });
        }
    });
}


function getCsrfToken() {
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    return csrfToken;
}