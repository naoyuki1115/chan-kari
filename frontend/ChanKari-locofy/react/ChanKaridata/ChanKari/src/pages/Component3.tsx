import { FunctionComponent, useCallback } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./Component3.module.css";

const Component3: FunctionComponent = () => {
  const navigate = useNavigate();

  const onButtonClick = useCallback(() => {
    navigate("/");
  }, [navigate]);

  return (
    <div className={styles.div}>
      <img className={styles.icon} alt="" src="../-11.svg" />
      <b className={styles.b}>チャンカリ</b>
      <div className={styles.div1}>
        <b className={styles.b1}>メールアドレス</b>
      </div>
      <div className={styles.div2}>
        <b className={styles.b1}>パスワード</b>
      </div>
      <div className={styles.div3}>
        <b className={styles.b1}>パスワード（確認）</b>
      </div>
      <button className={styles.button} onClick={onButtonClick}>
        <b className={styles.b4}>新規登録</b>
      </button>
    </div>
  );
};

export default Component3;
