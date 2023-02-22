import { Route, Routes } from "react-router-dom";
import "./App.css";
import BorrowList from "./component/BorrowList";
import NavTop from "./component/Header";
import Home from "./component/Home";
import ItemDetail from "./component/ItemDetail";
import ItemRegister from "./component/ItemRegister";
import MyItemList from "./component/MyItemList";
import MyPage from "./component/MyPage";
import NavBottom from "./component/Navigation";
import RentList from "./component/RentList";

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
