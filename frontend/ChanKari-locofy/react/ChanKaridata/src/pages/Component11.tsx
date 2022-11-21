import { FunctionComponent, useState, useCallback } from "react";
import Component2 from "../components/Component2";
import PortalPopup from "../components/PortalPopup";
import Component1 from "../components/Component1";
import { useNavigate } from "react-router-dom";
import styles from "./Component11.module.css";

const Component11: FunctionComponent = () => {
  const [isArtboardOpen, setArtboardOpen] = useState(false);
  const [isArtboard1Open, setArtboard1Open] = useState(false);
  const navigate = useNavigate();

  const openArtboard = useCallback(() => {
    setArtboardOpen(true);
  }, []);

  const closeArtboard = useCallback(() => {
    setArtboardOpen(false);
  }, []);

  const openArtboard1 = useCallback(() => {
    setArtboard1Open(true);
  }, []);

  const closeArtboard1 = useCallback(() => {
    setArtboard1Open(false);
  }, []);

  const onButton2Click = useCallback(() => {
    navigate("/");
  }, [navigate]);

  const onText1Click = useCallback(() => {
    navigate("/3");
  }, [navigate]);

  const onButton3Click = useCallback(() => {
    navigate("/3");
  }, [navigate]);

  return (
    <>
      <div className={styles.div}>
        <div className={styles.div1}>
          <img className={styles.icon} alt="" src="../-11.svg" />
          <button className={styles.button} onClick={openArtboard} />
          <button className={styles.button1} onClick={openArtboard1} />
          <button className={styles.button2} onClick={onButton2Click} />
        </div>
        <div className={styles.div2}>
          <img className={styles.icon1} alt="" src="../-11.svg" />
          <b className={styles.b}>チャンカリ</b>
        </div>
        <button className={styles.button3} onClick={onButton3Click}>
          <div className={styles.div3} onClick={onText1Click}>
            借りる
          </div>
        </button>
        <div className={styles.div4}>レンタル品名１</div>
        <div className={styles.div5}>【貸出者：　　　】</div>
        <div className={styles.div6}>
          <p className={styles.p}>詳細</p>
          <p className={styles.p}>
            ・・・・・・・・・・・・・・・・・・・・・・・・・・・
          </p>
          <p className={styles.p}>
            ・・・・・・・・・・・・・・・・・・・・・・・・・・・
          </p>
          <p className={styles.p}>
            ・・・・・・・・・・・・・・・・・・・・・・・・・・・
          </p>
          <p className={styles.p}>
            ・・・・・・・・・・・・・・・・・・・・・・・・・・・
          </p>
          <p className={styles.p}>&nbsp;</p>
        </div>
      </div>
      {isArtboardOpen && (
        <PortalPopup
          overlayColor="rgba(113, 113, 113, 0.3)"
          placement="Centered"
          onOutsideClick={closeArtboard}
        >
          <Component2 onClose={closeArtboard} />
        </PortalPopup>
      )}
      {isArtboard1Open && (
        <PortalPopup
          overlayColor="rgba(113, 113, 113, 0.3)"
          placement="Centered"
          onOutsideClick={closeArtboard1}
        >
          <Component1 onClose={closeArtboard1} />
        </PortalPopup>
      )}
    </>
  );
};

export default Component11;
