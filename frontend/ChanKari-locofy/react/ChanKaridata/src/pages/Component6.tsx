import { FunctionComponent, useState, useCallback } from "react";
import Component2 from "../components/Component2";
import PortalPopup from "../components/PortalPopup";
import Component1 from "../components/Component1";
import { useNavigate } from "react-router-dom";
import styles from "./Component6.module.css";

const Component6: FunctionComponent = () => {
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
        <div className={styles.div3}>
          <div className={styles.div4}>
            <div className={styles.div5}>レンタル品名１</div>
            <div className={styles.oKDiv}>貸出中</div>
            <img className={styles.icon2} alt="" src="../-11.svg" />
          </div>
          <div className={styles.div7}>
            <div className={styles.div5}>レンタル品名２</div>
            <div className={styles.oKDiv}>貸出OK</div>
            <img className={styles.icon2} alt="" src="../-11.svg" />
          </div>
          <div className={styles.div9}>
            <div className={styles.div5}>レンタル品名３</div>
            <div className={styles.oKDiv}>貸出中</div>
            <img className={styles.icon2} alt="" src="../-11.svg" />
          </div>
          <div className={styles.div12}>
            <div className={styles.div5}>レンタル品名</div>
            <div className={styles.oKDiv}>貸出OK</div>
            <img className={styles.icon2} alt="" src="../-11.svg" />
          </div>
          <div className={styles.div14}>
            <div className={styles.div5}>レンタル品名</div>
            <div className={styles.oKDiv}>貸出OK</div>
            <img className={styles.icon2} alt="" src="../-11.svg" />
          </div>
          <div className={styles.div16}>
            <div className={styles.div5}>レンタル品名</div>
            <div className={styles.oKDiv}>貸出中</div>
            <img className={styles.icon2} alt="" src="../-11.svg" />
          </div>
          <div className={styles.div19}>
            <div className={styles.div5}>レンタル品名</div>
            <div className={styles.oKDiv}>貸出中</div>
            <img className={styles.icon2} alt="" src="../-11.svg" />
          </div>
          <div className={styles.div22}>
            <div className={styles.div5}>レンタル品名</div>
            <div className={styles.oKDiv}>貸出中</div>
            <img className={styles.icon2} alt="" src="../-11.svg" />
          </div>
          <div className={styles.div25}>
            <div className={styles.div5}>レンタル品名</div>
            <div className={styles.oKDiv}>貸出中</div>
            <img className={styles.icon2} alt="" src="../-11.svg" />
          </div>
        </div>
        <div className={styles.div28}>登録品一覧</div>
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

export default Component6;
