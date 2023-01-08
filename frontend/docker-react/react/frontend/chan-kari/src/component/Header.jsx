import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import './Navigation.css';
import { faHome } from "@fortawesome/free-solid-svg-icons";
import { faPencil } from "@fortawesome/free-solid-svg-icons";
import { faUser } from "@fortawesome/free-solid-svg-icons";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import Dropdown from 'react-bootstrap/Dropdown';
import NavItem from 'react-bootstrap/NavItem';
import NavLink from 'react-bootstrap/NavLink';

function NavTop() {
    const handleSelect = (eventKey) => alert(`selected ${eventKey}`);

    return (
        <Navbar bg="light" >
            <Container>
                <Navbar.Brand href="/">チャンカリ</Navbar.Brand>
            </Container>
        </Navbar>
    );
}

//render(<NavDropdownExample />);
export default NavTop;