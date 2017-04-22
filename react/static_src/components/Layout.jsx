import React from 'react';
import { Nav, NavItem, Navbar, NavbarBrand, Grid, Row, Col } from 'react-bootstrap';

class Layout extends React.Component {

    state = {
        activeKey: 1
    };

    setActive = (eventKey) => {
        this.setState({
            activeKey: eventKey
        })
    };

    render() {
        return <div>
            <Navbar inverse>
                <Navbar.Header>
                    <NavbarBrand>Social Network</NavbarBrand>
                </Navbar.Header>

                <Nav activeKey={ this.state.activeKey }>
                    <NavItem eventKey={ 1 } onSelect={ this.setActive }>Моя страница</NavItem>
                    <NavItem eventKey={ 2 } onSelect={ this.setActive }>Новости</NavItem>
                    <NavItem eventKey={ 3 } onSelect={ this.setActive }>Друзья</NavItem>
                    <NavItem eventKey={ 4 } onSelect={ this.setActive }>Чаты</NavItem>
                    <NavItem eventKey={ 5 } onSelect={ this.setActive }>Люди</NavItem>
                </Nav>
            </Navbar>

            <div className="container">
                <Grid>
                    <Row>
                        <Col sm={1}/>
                        <Col sm={10}>
                            { this.props.activeKeyComponent(this.state.activeKey) }
                        </Col>
                        <Col sm={1}/>
                    </Row>
                </Grid>
            </div>

        </div>
    }
}

Layout.propTypes = {
    activeKeyComponent: React.PropTypes.func.isRequired,
};

export default Layout;