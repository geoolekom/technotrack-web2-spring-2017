import React from 'react';
import { ListGroupItem, Button } from 'react-bootstrap';

const little_letters = {
    fontSize: 10,
};


class Friend extends React.Component {
    render() {
        if (this.props.status === 'friend') {
            return <ListGroupItem header={ this.props.name } style={ little_letters }>Друг</ListGroupItem>
        } else if (this.props.status === 'incoming') {
            return <ListGroupItem bsStyle="info" header={ this.props.name } style={ little_letters }>
                Входящая заявка<br/><br/>
                <Button>Принять</Button>
                <span><Button>Отказать</Button></span>
            </ListGroupItem>
        } else if (this.props.status === 'outgoing') {
            return <ListGroupItem bsStyle="warning" header={ this.props.name } style={ little_letters }>
                Исходящая заявка<br/><br/>
                <Button>Отменить</Button>
            </ListGroupItem>
        }
    }
}

Friend.propTypes = {
    name: React.PropTypes.string.isRequired,
    status: React.PropTypes.string.isRequired
};

export default Friend;