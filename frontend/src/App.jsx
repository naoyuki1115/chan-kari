import { BrowserRouter, Route, Routes } from "react-router-dom";
import { Fragment } from "react";
import ReactDOM from "react-dom";
import "./App.css";
import Home from "./component/Home";
import NavBottom from "./component/Navigation";
import NavTop from "./component/Header";
import MyPage from "./component/MyPage";
import RentList from "./component/RentList";
import BorrowList from "./component/BorrowList";
import MyItemList from "./component/MyItemList";
import ItemRegister from "./component/ItemRegister";
import ItemDetail from "./component/ItemDetail";

export const App = () => (
    <div className="App">
        <NavTop />
        <Routes>
            <Route path={"/"} element={<Home />} />
            <Route path={"/mypage"} element={<MyPage />} />
            <Route path={"/RentList"} element={<RentList />} />
            <Route path={"/BorrowList"} element={<BorrowList />} />
            <Route path={"/MyItemList"} element={<MyItemList />} />
            <Route path={"/ItemRegister"} element={<ItemRegister />} />
            <Route path={"/ItemDetail/:id"} element={<ItemDetail />} />
        </Routes>
        <NavBottom />
        <div className="App-Spacer"></div>
    </div>
);
