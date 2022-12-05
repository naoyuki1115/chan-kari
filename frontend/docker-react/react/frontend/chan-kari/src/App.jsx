import { Fragment } from "react";
import ReactDOM from "react-dom"
import './App.css';


export const App = () => {
  return (
    <Fragment>
      <h1>チャンカリ</h1>
      <p>ホームページ</p>
    </Fragment>

  );
};

ReactDOM.render(<App />, document.getElementById("root"));


