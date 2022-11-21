import { FunctionComponent, useCallback } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./Component2.module.css";

type Component2Type = {
  onClose?: () => void;
};

const Component2: FunctionComponent<Component2Type> = ({ onClose }) => {
  const navigate = useNavigate();

  const onTextClick = useCallback(() => {
    navigate("/4");
  }, [navigate]);

  const onButtonClick = useCallback(() => {
    navigate("/4");
  }, [navigate]);

  const onText1Click = useCallback(() => {
    navigate("/5");
  }, [navigate]);

  const onButton1Click = useCallback(() => {
    navigate("/5");
  }, [navigate]);

  return (
    <div className={styles.div}>
      <button className={styles.button} onClick={onButtonClick}>
        <div className={styles.div1} onClick={onTextClick}>
          貸出品新規登録
        </div>
      </button>
      <button className={styles.button1} onClick={onButton1Click}>
        <div className={styles.div1} onClick={onText1Click}>
          登録品リスト
        </div>
      </button>
    </div>
  );
};

export default Component2;
