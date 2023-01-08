import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { Fragment } from "react";
import ReactDOM from "react-dom"
import './App.css';
import Home from './component/Home';
import NavBottom from './component/Navigation';

export const App = () => {
  return (
    <div className="App">
      <div>
        <h1>チャンカリ</h1>
      </div>

      <NavBottom />

      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
      <Routes>
        <Route path="/item_register" element={<Item_register />} />
      </Routes>
      <Routes>
        <Route path="/mypage" element={<Mypage />} />
      </Routes>

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


