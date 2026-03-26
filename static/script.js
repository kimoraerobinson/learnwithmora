let score = 0;
let total = 10;
let current;

function stars() {
    let div = document.getElementById("stars");
    div.innerHTML = "";
    for (let i = 0; i < total; i++) {
        let s = document.createElement("span");
        s.innerHTML = "★";
        s.className = "star";
        if (i < score) s.classList.add("active");
        div.appendChild(s);
    }
}

function progress() {
    document.getElementById("bar").style.width = (score/total)*100 + "%";
}

function load() {
    fetch("/get-question")
    .then(r=>r.json())
    .then(d=>{
        if (d.finished) {
            window.location="/results";
            return;
        }
        current = d;
        document.getElementById("question").innerText = d.question;
        document.querySelectorAll(".opt").forEach((b,i)=>{
            b.innerText = d.options[i];
            b.disabled=false;
        });
    });
}

document.querySelectorAll(".opt").forEach(b=>{
    b.onclick = function() {
        fetch("/check-answer", {
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify({
                question: current.question,
                selected: this.innerText,
                topic: current.topic
            })
        })
        .then(r=>r.json())
        .then(res=>{
            document.getElementById("feedback").innerText = res.correct ? "✅ Correct" : "❌ Wrong";
            if(res.correct) score++;
            stars();
            progress();
            document.querySelectorAll(".opt").forEach(b=>b.disabled=true);
        });
    }
});

document.getElementById("next").onclick = load;

load();
stars();
progress();