import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { Fragment } from "react";
import ReactDOM from "react-dom"
import './App.css';
import Home from './component/Home';
import NavBottom from './component/Navigation';
import NavTop from './component/Header';
import MyPage from './component/MyPage';
import RentList from './component/RentList';
import BorrowList from './component/BorrowList';
import MyItemList from './component/MyItemList';

export const App = () => {
  return (
    <div className="App">
      <NavTop />


      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
      <Routes>
        <Route path="/item_register" element={<Item_register />} />
      </Routes>
      <Routes>
        <Route path="/mypage" element={<MyPage />} />
      </Routes>
      <Routes>
        <Route path="/RentList" element={<RentList />} />
      </Routes>
      <Routes>
        <Route path="/BorrowList" element={<BorrowList />} />
      </Routes>
      <Routes>
        <Route path="/MyItemList" element={<MyItemList />} />
      </Routes>

      <NavBottom />
    </div>
  );
};



function Item_register() {
  return <h2>貸出登録</h2>;
}





//ReactDOM.render(<App />, document.getElementById("root"));


