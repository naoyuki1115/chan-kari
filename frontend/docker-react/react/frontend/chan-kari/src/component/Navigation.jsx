import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import './Navigation.css';
import { faHome } from "@fortawesome/free-solid-svg-icons";
import { faPencil } from "@fortawesome/free-solid-svg-icons";
import { faUser } from "@fortawesome/free-solid-svg-icons";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import Dropdown from 'react-bootstrap/Dropdown';
import NavItem from 'react-bootstrap/NavItem';
import NavLink from 'react-bootstrap/NavLink';



const homeUrl = process.env.PUBLIC_URL;

function NavBottom() {
    const handleSelect = (eventKey) => alert(`selected ${eventKey}`);

    return (
        <Navbar bg="light" expand="lg" fixed='bottom'>
            <Container>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">

                    <Nav className="me-auto">
                        <Nav.Link href={homeUrl}>
                            <p><FontAwesomeIcon icon={faHome} /></p>
                            HOME
                        </Nav.Link>

                        <Dropdown as={NavItem} drop='up'>
                            <Dropdown.Toggle as={NavLink}>
                                <p><FontAwesomeIcon icon={faPencil} /></p>
                                登録
                            </Dropdown.Toggle>
                            <Dropdown.Menu>
                                <Dropdown.Item href={homeUrl + "/ItemRegister"}>貸出品新規登録</Dropdown.Item>
                                <Dropdown.Item href={homeUrl + "/MyItemList"}>登録品リスト</Dropdown.Item>
                            </Dropdown.Menu>
                        </Dropdown>

                        <Nav.Link href={homeUrl + "/Mypage"}>
                            <p><FontAwesomeIcon icon={faUser} /></p>
                            マイページ
                        </Nav.Link>


                    </Nav>

                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}

//render(<NavDropdownExample />);
export default NavBottom;