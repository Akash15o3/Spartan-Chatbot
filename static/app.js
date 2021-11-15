class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button'),
//            uploadButton: document.querySelector('.image_input')
        }

        this.state = false;
        this.messages = [];
//        this.image = "";
    }

    display() {
        const {openButton, chatBox, sendButton, uploadButton} = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBox))

        sendButton.addEventListener('click', () => this.onSendButton(chatBox))

//        uploadButton.addEventListener('change', () => this.onUploadButton(chatBox))

        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", ({key}) => {
            if (key === "Enter") {
                this.onSendButton(chatBox)
            }
        })
    }

    toggleState(chatbox) {
        this.state = !this.state;

        // show or hides the box
        if(this.state) {
            chatbox.classList.add('chatbox--active')
        } else {
            chatbox.classList.remove('chatbox--active')
        }
    }

    onSendButton(chatbox) {
        var textField = chatbox.querySelector('input');
        let text1 = textField.value
        if (text1 === "") {
            return;
        }

        let msg1 = { name: "User", message: text1 }
        this.messages.push(msg1);

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
            let msg2 = { name: "SpartanBot", message: r.answer };
            this.messages.push(msg2);
            this.updateChatText(chatbox)
            textField.value = ''

        }).catch((error) => {
            console.error('Error:', error);
            this.updateChatText(chatbox)
            textField.value = ''
          });
    }

    onUploadButton(chatbox) {
    var images = [];
    var image = document.getElementById('image_input');
    console.log(image);
//        const reader = new FileReader();
//        this.image = reader.result;
//        console.log(this.image);
//        reader.addEventListener("load", () => {
//        console.log("IN HERE");
//        this.image = reader.result;
//        console.log(this.image);
//        document.querySelector("#display_image").style.backgroundImage = `url(${this.image})`;
//
//        });
//        reader.readAsDataURL(this.files);
//        var html = '';
//             html += '<img src="static/images/imagebutton.png">' + "hellotherie" + '</div>'
//
//            const chatmessage = chatbox.querySelector('.chatbox__messages');
//            chatmessage.innerHTML = html;
    }

    updateChatText(chatbox) {
        var html = '';
        this.messages.slice().reverse().forEach(function(item, index) {
           if (item.name === "SpartanBot")
            {
                html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
            }

//            {
//                html += '<img src="static/images/imagebutton.png">' + item.message + '</div>'
//            }

            else
            {
                html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
            }
          });

        const chatmessage = chatbox.querySelector('.chatbox__messages');
        chatmessage.innerHTML = html;
    }
}


const chatbox = new Chatbox();
chatbox.display();