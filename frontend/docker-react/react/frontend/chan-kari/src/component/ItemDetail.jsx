
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Alert from 'react-bootstrap/Alert';
import Card from 'react-bootstrap/Card';
import { useParams } from 'react-router-dom'
import { useLocation } from "react-router-dom";

function ItemDetail() {
    const { id } = useParams()
    const location = useLocation();
    console.log(location)

    return (
        <Container>

            <h3>レンタル品詳細</h3>
            <Row >
                <Col></Col>
                <Col xs={5}>
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

            </Row>

        </Container>

    );
};

export default ItemDetail;