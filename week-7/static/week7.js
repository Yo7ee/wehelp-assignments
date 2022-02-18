    //用於取得<article>元素的參考，並將其儲存於變數中
let aside = document.querySelector('aside');
let src="http://127.0.0.1:3000/api/members"

// 透過AJAX fetch API連線到遠端的網址，抓取資料
// fetch(網址).then(function(response){
//     Response物件，代表伺服器的回應
// })

// 把抓到的資料放在畫面
function searchName(){
    let username=document.querySelector('#username').value;
    let checkP=document.querySelector('p');
    const data= fetch("http://127.0.0.1:3000/api/members?username="+username) //將變數傳入網址，直接在網址後面+變數名稱
        // {method:'post', body: jsonUsername}) 適用要求三
    .then(function(response){
        return response.json(); //不確定能否直接將list轉換成json格式
});
// // console.log(data) //資料型態為object
//     data.then(function(jsonObj){
//         let name = jsonObj.data.name; //想辦法取得object內的資料
//         // console.log(name)
//         // let p =document.createElement('p');
//         p.textContent=name + ' (' + username + ')';
//         aside.appendChild(p);
//     });
    if (username.length==0){
        return;
    }else if(checkP==null){
        console.log(checkP)
        data.then(function(jsonObj){
            let name = jsonObj.data.name; //想辦法取得object內的資料
            let p =document.createElement('p');
            // console.log(name)
            // let p =document.createElement('p');
            p.textContent=name + ' (' + username + ')';
            aside.appendChild(p);
        });
    }else{ 
        console.log(username)
        data.then(function(jsonObj){
            let name = jsonObj.data.name; //想辦法取得object內的資料
            let newP =document.createElement('p');
            let p = document.querySelector('p');
            newP.textContent=name + ' (' + username + ')';
            p.remove(p);
            aside.appendChild(newP);
        });
    };
};
