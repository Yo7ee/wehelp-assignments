//用於取得<article>元素的參考，並將其儲存於變數中
let article=document.querySelector('article');
//將JSON檔案儲存起來
let requestURL = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
//為了建立需求，須透過"new"關鍵字，先從XMLHttpRequest建構新的請求物件
let request = new XMLHttpRequest();
//用open函式開啟新的請求.open(method, url),用什麼方法打開哪個位址
request.open('GET', requestURL);
//我們為JSON設定"responseType，告知伺服器應回傳JSON物件，再以send()函式傳送請求
request.responseType = "json";
request.send();
//最後就是等待由伺服器所回傳的反應，再接著處理
//我們在此將所獲的的響應(response)儲存到siteList變數中
//接著把此JSON檔案送到1個函式呼叫中，第一個函式呼叫會將圖片位址填入<img>及圖片名稱填入<figcaption>
request.onload = function(){
    let siteList =request.response;
    populateImg(siteList);
}
//將上述的函式寫出來
function populateImg(jsonObj){
    let list=jsonObj.result.results;
    //只顯示8張圖片
    for( let i=0; i<8; i++){
    let myFigure = document.createElement('figure');
    let myImg = document.createElement('img');//建立一組<img>元素，將其text.content指定為JSON的file屬性、透過appendChild將之附加到圖片
    let myFigcaption = document.createElement('figcaption');//建立一組<figcaption>元素，將其text.content指定為JSON的file屬性、透過appendChild將之附加到圖片
    let modContent= list[i].file.toLowerCase();
    let imgUrlList = modContent.split("jpg",1)+"jpg";
    myFigcaption.textContent=list[i].stitle;
    myImg.src=imgUrlList;//新增圖片網址屬性至<img>
    myFigure.appendChild(myImg);
    myFigure.appendChild(myFigcaption);

    article.appendChild(myFigure);
    };
};