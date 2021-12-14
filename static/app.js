const openBtn      = document.querySelector('.chatbox__btn');
const chatBox      = document.querySelector('.chatbox__support');
const sendBtn      = document.querySelector('.send__btn');
const input        = document.querySelector('input');
const chatmessage  = document.querySelector('.chatbox__messages');
const greeting     = document.querySelectorAll('.messages__greeting');

let messages = [];
let state = false;


const display = () => {
    openBtn.addEventListener('click', () => toggleState())
    
    sendBtn.addEventListener('click', () => onSendButton())

    input.addEventListener("keyup", ({key}) => {
        if (key === "Enter") {
            onSendButton()
        }
    })
}

const toggleState = () => {
    state = !state;

    // show or hides the box
    if(state) {
        chatBox.classList.add('chatbox--active')
        greeting.forEach((cadaGreeting, i) => {
            greeting[i].classList.add('active')
        })
    } else {
        chatBox.classList.remove('chatbox--active')
        greeting.forEach((cadaGreeting, i) => {
            greeting[i].classList.remove('active')
        })
    }
}

const onSendButton = () => {
    let text1 = input.value
    if (text1 === "") {
        return;
    }

    let msg1 = { name: "User", message: text1 }
    messages.push(msg1);

    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        body: JSON.stringify({ message: text1 }),
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json'
        },
      })
      .then(r => r.json())
      .then(r => {
        updateChatText(text1, r.answer);
        input.value = ''

    }).catch((error) => {
        console.error('Error:', error);
        updateChatText()
        input.value = ''
      });
}

const updateChatText = (input, bot) => {
    
    let userDiv = document.createElement("div");
        userDiv.className = "messages__item messages__item--operator";
        userDiv.innerHTML = `${input}`;
        chatmessage.appendChild(userDiv);
   
    let botDiv = document.createElement("div");
        botDiv.className = "messages__item messages__item--visitor";
        botDiv.innerHTML = `<div class="loader">
                                <div class="loader__dot"></div>
                                <div class="loader__dot"></div>
                                <div class="loader__dot"></div>
                            </div>`;                  
        chatmessage.appendChild(botDiv);
                              
    setTimeout(() => {
      botDiv.innerText = `${bot}`;
    }, 1500); 
}

display();