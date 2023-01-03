import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { Fragment } from "react";
import ReactDOM from "react-dom"
import './App.css';


export const App = () => {
  return (
    <div className="App">
      <div>
        <h1>チャンカリ</h1>
        <p>ホームページ</p>
      </div>

      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
    </div>
  );
};

function Home() {
  return <h2>Home</h2>;
}

function About() {
  return <h2>About</h2>;
}

function Contact() {
  return <h2>Contact</h2>;
}



//ReactDOM.render(<App />, document.getElementById("root"));


