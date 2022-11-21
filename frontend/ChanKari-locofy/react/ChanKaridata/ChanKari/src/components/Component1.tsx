import { FunctionComponent, useCallback } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./Component1.module.css";

type Component1Type = {
  onClose?: () => void;
};

const Component1: FunctionComponent<Component1Type> = ({ onClose }) => {
  const navigate = useNavigate();

  const onButtonClick = useCallback(() => {
    navigate("/2");
  }, [navigate]);

  const onButton1Click = useCallback(() => {
    navigate("/3");
  }, [navigate]);

  return (
    <div className={styles.div}>
      <button className={styles.button} onClick={onButtonClick}>
        <div className={styles.div1}>貸しているもの</div>
      </button>
      <button className={styles.button1} onClick={onButton1Click}>
        <div className={styles.div1}>借りているもの</div>
      </button>
    </div>
  );
};

export default Component1;
