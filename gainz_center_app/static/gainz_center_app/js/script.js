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