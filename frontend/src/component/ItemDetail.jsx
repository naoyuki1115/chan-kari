import React from "react";
import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";
import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
import Modal from "react-bootstrap/Modal";
import Row from "react-bootstrap/Row";
import { useLocation, useParams } from "react-router-dom";

function ItemDetail() {
  const { id } = useParams();
  const location = useLocation();

  console.log(location);

  return (
    <Container>
      <h3>レンタル品詳細</h3>
      <Row>
        <Col></Col>
        <Col xs={12} md={5}>
          <Card>
            <Card.Img variant="top" src="https://placehold.jp/100x40.png" />
            <Card.Body>
              <Card.Title>タイトル：●●●</Card.Title>
              <Card.Text>
                <h3>id:{id}</h3>
                <p>著者</p>
                <p>【詳細】</p>
                <p>×××××××××××××××</p>
                <p>×××××××××××××××</p>
                <p>【貸出者：○○○】</p>
              </Card.Text>
            </Card.Body>
          </Card>
        </Col>
        <Col></Col>
      </Row>
      <Row>
        <h2>{location.state.fromPage}</h2>
        <ButtonSelect frompage={location.state.fromPage} />
      </Row>
    </Container>
  );
}

const ButtonSelect = (props) => {
  const [returnModalShow, setReturnModalShow] = React.useState(false);
  const [rentModalShow, setRentModalShow] = React.useState(false);
  const buttonSelector = (frompageName) => {
    switch (frompageName) {
      case "HomePage":
        return (
          <div>
            <p>貸出可能 or 貸出中</p>
            <Button variant="primary" onClick={() => setRentModalShow(true)}>
              借りる
            </Button>
            <RentConfirmModal
              show={rentModalShow}
              onHide={() => setRentModalShow(false)}
            />

            <Button variant="primary" disabled>
              借りる
            </Button>
          </div>
        );

      case "MyItemList":
        return (
          <div>
            <p>貸出可能 or 貸出中</p>
            <Button variant="primary" href={"/ItemRegister"}>
              編集
            </Button>

            <Button variant="primary" onClick={() => setReturnModalShow(true)}>
              返却済み
            </Button>

            <ReturnConfirmModal
              show={returnModalShow}
              onHide={() => setReturnModalShow(false)}
            />
          </div>
        );
      case "BorrowList":
        return (
          <div>
            <p>レンタル中</p>

            <Button variant="primary" onClick={() => setReturnModalShow(true)}>
              返却済み
            </Button>

            <ReturnConfirmModal
              show={returnModalShow}
              onHide={() => setReturnModalShow(false)}
            />
          </div>
        );

      case "RentList":
        return (
          <div>
            <p>貸出中</p>
          </div>
        );

      default:
        console.log(frompageName.frompage);
        return <p>デフォルト</p>;
    }
  };

  return <>{buttonSelector(props.frompage)}</>;
};

function ReturnConfirmModal(props) {
  return (
    <Modal
      {...props}
      size="lg"
      aria-labelledby="contained-modal-title-vcenter"
      centered
    >
      <Modal.Header closeButton>
        <Modal.Title id="contained-modal-title-vcenter">
          返却しますか
        </Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <h4>タイトル</h4>
      </Modal.Body>
      <Modal.Footer>
        <Button>返却</Button>
        <Button onClick={props.onHide}>Close</Button>
      </Modal.Footer>
    </Modal>
  );
}

function RentConfirmModal(props) {
  return (
    <Modal
      {...props}
      size="lg"
      aria-labelledby="contained-modal-title-vcenter"
      centered
    >
      <Modal.Header closeButton>
        <Modal.Title id="contained-modal-title-vcenter">借りますか</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <h4>タイトル</h4>
        <p>貸出し期間は２週間です。</p>
      </Modal.Body>
      <Modal.Footer>
        <Button>借りる</Button>
        <Button onClick={props.onHide}>Close</Button>
      </Modal.Footer>
    </Modal>
  );
}

export default ItemDetail;
