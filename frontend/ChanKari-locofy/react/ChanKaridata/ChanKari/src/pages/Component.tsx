import { FunctionComponent, useCallback } from "react";
import { useNavigate, Link } from "react-router-dom";
import styles from "./Component.module.css";

const Component: FunctionComponent = () => {
  const navigate = useNavigate();

  const onButtonClick = useCallback(() => {
    navigate("/");
  }, [navigate]);

  const onLinkClick = useCallback(() => {
    navigate("/1");
  }, [navigate]);

  return (
    <div className={styles.div}>
      <img className={styles.icon} alt="" src="../-1@2x.png" />
      <textarea className={styles.textarea} />
      <textarea className={styles.textarea1} />
      <button className={styles.button} onClick={onButtonClick}>
        <b className={styles.b}>ログイン</b>
      </button>
      <Link className={styles.a} to="/1" onClick={onLinkClick}>
        会員登録
      </Link>
      <div className={styles.div1}>
        <img className={styles.icon1} alt="" src="../-11.svg" />
        <b className={styles.b1}>チャンカリ</b>
      </div>
    </div>
  );
};

export default Component;
