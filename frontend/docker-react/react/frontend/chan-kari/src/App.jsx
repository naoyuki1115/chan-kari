import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { Fragment } from "react";
import ReactDOM from "react-dom"
import './App.css';
import Home from './component/Home';

export const App = () => {
  return (
    <div className="App">
      <div>
        <h1>チャンカリ</h1>
      </div>

      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
      <Routes>
        <Route path="/item_register" element={<Item_register />} />
      </Routes>
      <Routes>
        <Route path="/mypage" element={<Mypage />} />
      </Routes>

      <dev className="menu">
        <h3>メニュー</h3>
        <ul>
          <li>
            <a href="/">ホーム</a>
          </li>
          <li>
            <a href="/item_register">登録</a>
          </li>
          <li>
            <a href="/mypage">マイページ</a>
          </li>
        </ul>

      </dev>
    </div>
  );
};



function Item_register() {
  return <h2>貸出登録</h2>;
}

function Mypage() {
  return <h2>マイページ</h2>;
}



//ReactDOM.render(<App />, document.getElementById("root"));


