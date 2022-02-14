// 透過AJAX fetch API連線到遠端的網址，抓取資料
// fetch(網址).then(function(response){
//     Response物件，代表伺服器的回應
// })


//用於取得<article>元素的參考，並將其儲存於變數中
let article=document.querySelector('article');
// 第一個then,連線網址抓到第一個程式response物件，在解析response物件，用字串換的方式取回主要資料，
// 第二個then, 主要資料會出現在result裡
let src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
const data =
fetch(src).then(function(response){
    // return response.text(); //用字串的方式取回資料，但字串很難用
    return response.json(); //將資料用JSON的格式詮釋成：物件和陣列的組合
});

data.then(function(jsonObj){
    // console.log("最終的資料", result)
    // 把抓到的資料放在畫面
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
});


function loadMore(){
    data.then(function(jsonObj){
        let list=jsonObj.result.results;
        // let htmlTagCount = document.getElementsByTagName('figcaption'); 
        // 這個無法使用，因為for迴圈原本只要跑8次，但這個程式是live自動更新，當第一次迴圈跑完，htmltagcount就會馬上增加一，所以就會直接跑到全部跑完為止
        //載入更多圖片，設定一次多8張圖片
        let htmlTagCount= document.querySelectorAll('figure')
        console.log(htmlTagCount)
        for( let i=htmlTagCount.length; i<htmlTagCount.length+8; i++){
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
    })
};    



