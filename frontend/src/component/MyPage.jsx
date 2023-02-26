import Col from "react-bootstrap/Col";
import Container from "react-bootstrap/Container";
import Image from "react-bootstrap/Image";
import ListGroup from "react-bootstrap/ListGroup";
import Row from "react-bootstrap/Row";

function MyPage() {
  return (
    <Container>
      <Row>
        <Col>
          <Image roundedCircle="true" src="https://placehold.jp/100x100.png" />
          <p>NAME: 名前</p>
          <p>ID : ※※※※※※※</p>
        </Col>
      </Row>

      <Row>
        <ListGroup defaultActiveKey="#link1">
          <ListGroup.Item action href={"/RentList"}>
            貸しているものリスト
          </ListGroup.Item>
          <ListGroup.Item action href={"/BorrowList"}>
            借りているものリスト
          </ListGroup.Item>
        </ListGroup>
      </Row>
    </Container>
  );
}

export default MyPage;
