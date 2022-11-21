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
      <textarea className={styles.textarea} />
      <textarea className={styles.textarea1} />
      <textarea className={styles.textarea2} />
      <button className={styles.button} onClick={onButtonClick}>
        <b className={styles.b1}>新規登録</b>
      </button>
    </div>
  );
};

export default Component3;
