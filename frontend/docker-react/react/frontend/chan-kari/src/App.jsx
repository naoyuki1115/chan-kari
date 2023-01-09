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
import ItemRegister from './component/ItemRegister';
import ItemDetail from './component/ItemDetail';

const homeUrl = process.env.PUBLIC_URL;

export const App = () => {
  return (
    <div className="App">
      <NavTop />



      <Routes>
        <Route path={homeUrl} element={<Home />} />
      </Routes>
      <Routes>
        <Route path={homeUrl + "/mypage"} element={<MyPage />} />
      </Routes>
      <Routes>
        <Route path={homeUrl + "/RentList"} element={<RentList />} />
      </Routes>
      <Routes>
        <Route path={homeUrl + "/BorrowList"} element={<BorrowList />} />
      </Routes>
      <Routes>
        <Route path={homeUrl + "/MyItemList"} element={<MyItemList />} />
      </Routes>
      <Routes>
        <Route path={homeUrl + "/ItemRegister"} element={<ItemRegister />} />
      </Routes>

      <Routes>
        <Route path={homeUrl + "/ItemDetail/:id"} element={<ItemDetail />} />
      </Routes>

      <Routes>
        <Route path="/" element={<Home />} />
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
      <Routes>
        <Route path="/ItemRegister" element={<ItemRegister />} />
      </Routes>

      <NavBottom />
    </div>
  );
};








//ReactDOM.render(<App />, document.getElementById("root"));


