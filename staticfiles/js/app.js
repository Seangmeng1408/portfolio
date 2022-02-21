
function scrollResponed(){
    var nav=document.getElementsByClassName("Nav")[0]
    window.addEventListener("scroll",(e)=>{
        if(window.scrollY>0){
            nav.style.position="fixed";
        }else {
            nav.style.position="";
        }
    })
}
scrollResponed();
function darkMode(){

    var darkmode=document.getElementById("dark-mode");
    var dMode=document.getElementById("d-mode");
    darkmode.addEventListener("click",()=>{
        dMode.classList.toggle("dark-active");
        if (dMode.classList.contains("dark-active")){
            dMode.href=staticCss+ "/darkmode.css";
            darkmode.innerText="L";
        }else{
            dMode.href="";
            darkmode.innerText="D"
        }
        
    })
    
    
}
darkMode();
function khmermode(){
    var khmerobj={greeting:["ស្វាគមន៍មកកាន់ Portfolio របស់ខ្ញុំ",
    "ខ្ញុំ ស៊ាងម៉េង. ជំរាបសួរ! ពីព្រះរាជាណាចក្រកម្ពុជា"],
    about:["អំពីខ្ញុំ!",
    "ខ្ញុំជា និស្សិតឆ្នាំទី៣ នៅវិទ្យាស្ថានបច្ចេកវិទ្យាកម្ពុជាជំនាញ វិស្វកម្មទេពកោសល្យពត៌មានវិទ្យា និងទំនាក់ទំនង។ ខ្ញុំចូលចិត្ដការអាន ការសរសេរកូដ និង សេរីភាព។ ខ្ញុំសង្ឃឹមថាយើងអាចរាប់អានគ្នាតាមបណ្ដាញសង្គមខ្ញុំនៅខាងក្រោមបាន ។សូមសំណាងល្អ!អគុណ!"],
    copy:"រក្សារសិទ្ធដោយ ឌិន ស៊ាងម៉េង"
}
document.getElementsByClassName("sub-greeting")[0].innerText=khmerobj.greeting[0];
document.getElementsByClassName("sub-greeting")[1].innerText=khmerobj.greeting[1];
document.getElementsByClassName("sub-about")[0].innerText=khmerobj.about[0];
document.getElementsByClassName("sub-about")[1].innerText=khmerobj.about[1];
document.getElementsByClassName("Copyright")[0].innerText=khmerobj.copy;
}
function englishmode(){
    var khmerobj={greeting:["Welcome To My Portfolio !!!",
    "I'm SEANGMENG DIN. Hello from Cambodia Kingdom of Wonder"],
    about:["About Me",
    "I'm Student at ITC at degree \"Information of Technology and Communication Engineering\".I'm Love Coding ,reading and love free life.Hope You love it. We can make friend with each other.My socail profile at the bottom.Have a greet day my friend!"],
    copy:"© Copy right by : DIN SEANGMENG"
}
document.getElementsByClassName("sub-greeting")[0].innerText=khmerobj.greeting[0];
document.getElementsByClassName("sub-greeting")[1].innerText=khmerobj.greeting[1];
document.getElementsByClassName("sub-about")[0].innerText=khmerobj.about[0];
document.getElementsByClassName("sub-about")[1].innerText=khmerobj.about[1];
document.getElementsByClassName("Copyright")[0].innerText=khmerobj.copy;
}
function LangSwitch(){
    var lang=document.getElementById("lag-mode");
    lang.addEventListener("click",()=>{
        lang.classList.toggle("khmer-active");
        if(lang.classList.contains("khmer-active")){
            khmermode();
            lang.innerText="EN"
        }else{
            englishmode();
            lang.innerText="KH"
            
        }
    })
}
LangSwitch()
function addActive(ele,position){
    for(let i=0;i<ele.length;i++){
        ele[i].classList.remove("active")
    }
    ele[position].classList.add("active")
}
function activeNav(){
    var navele=document.getElementsByClassName("navele");
    document.getElementsByClassName("nav_list")[0].addEventListener("click",(e)=>{
        const target=e.target.classList;
        if(!target.contains("active")){
            for(let i=0;i<navele.length;i++){
                navele[i].classList.remove("active")
            }
            target.add("active")
        }
    })
}


function autoSwitchActive(){
    var home=document.getElementsByClassName("Head-Container")[0]
    var about=document.getElementsByClassName("About-Container")[0]
    var achievment=document.getElementsByClassName("achievment-container")[0]
    var navele=document.getElementsByClassName("navele");
    var totalheight=home.clientHeight+about.clientHeight;
    window.addEventListener("scroll",(e)=>{
        if(window.scrollY>(totalheight-(about.clientHeight/1.5) +achievment.clientHeight)){
            addActive(navele,3);
        }
        else if(window.scrollY>=totalheight-(about.clientHeight/2) ){
            addActive(navele,2)
        }
        else if(window.scrollY>home.clientHeight-(home.clientHeight/3) ){
            addActive(navele,1);
        }
        else if(window.scrollY<home.clientHeight  ){
            addActive(navele,0);
        }
        
    })
}
autoSwitchActive()
activeNav()
