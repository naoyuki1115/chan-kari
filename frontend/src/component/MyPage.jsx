
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Alert from 'react-bootstrap/Alert';
import Card from 'react-bootstrap/Card';
import Image from 'react-bootstrap/Image'
import ListGroup from 'react-bootstrap/ListGroup';

const homeUrl = process.env.PUBLIC_URL;

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
                    <ListGroup.Item action href={homeUrl + "/RentList"}>
                        貸しているものリスト
                    </ListGroup.Item>
                    <ListGroup.Item action href={homeUrl + "/BorrowList"}>
                        借りているものリスト
                    </ListGroup.Item>

                </ListGroup>
            </Row>
        </Container>
    );
};

export default MyPage;