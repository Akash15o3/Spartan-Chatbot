class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button'),
            uploadButton: document.querySelector('.image_input')
        }

        this.state = false;
        this.messages = [];
        this.images = [];
    }

    display() {
        const {openButton, chatBox, sendButton, uploadButton} = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBox))

        sendButton.addEventListener('click', () => this.onSendButton(chatBox))

        uploadButton.addEventListener('change', () => this.onUploadButton(chatBox))

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

    var textField = chatbox.querySelector('input');
    let text2 = textField.value;
    console.log(text2);
    this.messages.push({name:"User" , message : text2});
    var image = document.getElementById('image').files;
    console.log("IMAGGGGG");
    console.log(URL.createObjectURL(image[0]));
    this.messages.push({name:"User" , message : URL.createObjectURL(image[0])});
    var text1 = '';
    text1 = "/Users/aaggarwal/Desktop/college_project/Spartan-Chatbot/Main_Page_Images/"+image[0].name;
        fetch('http://127.0.0.1:5000/predictimage', {
            method: 'POST',
            body: JSON.stringify({ image: text1 , message : text2 }),
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


    enlargeImage(html){
    console.log("INSNjsns");
    var modalImg = document.getElementById("img01");

        img.onclick = function(){
            modal.style.display = "block";
            modalImg.src = this.src;

        }
        // Get the <span> element that closes the modal
        var span = document.getElementsByClassName("close")[0];

        // When the user clicks on <span> (x), close the modal
        span.onclick = function() {
            modal.style.display = "none";
        }
    }

    updateChatText(chatbox) {
        var html = '';
        console.log("THIS MESSAGES");
        console.log(this.messages);
        this.messages.slice().reverse().forEach(function(item, index) {
           if (item.name === "SpartanBot"){

                      if(item.message.search('/Users')===0){
                      var str = item.message;
                      var x = '';
                      x = str.split(".");
                      x = x[0]+".jpeg"
                      str = str.substring(str.indexOf(".") + 1);
                      console.log("Item has image");
                      console.log(item.message);
                    html += '<div class="messages__item messages__item--visitor"> <img src="' + "static/images/2-modified.png" + '" alt=Imagee> </div>';
                     html += '<div class="messages__item messages__item--visitor">' + str + '</div>';

                 }
                 else {
                    html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
                 }
           }


//            {
//                html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
////                html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'"Anything else I can help you with"
//            }

            else
            {   if(item.message.search('blob')===0){
                    html += '<div class="messages__item messages__item--operator"> <img src="' + item.message + '" alt=Imagee> </div>'

                 }
                 else {
                    html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
                 }

            }
          });

        const chatmessage = chatbox.querySelector('.chatbox__messages');
        chatmessage.innerHTML = html;

    }
}


const chatbox = new Chatbox();
chatbox.display();