import React from 'react';
import $ from 'jquery';
import { ListGroupItem, ListGroup } from "react-bootstrap";

import storage from '../Storage'

class FriendList extends React.Component {

    state = {
        friends: [],
        requests: [],
        isLoading: true
    };

    render() {
        if (this.state.isLoading) {
            return <div>Идет загрузка...</div>
        } else {
            return <ListGroup>
                { this.state.requests }
                { this.state.friends }
            </ListGroup>
        }
    }

    componentDidMount = () => {

        storage.getData('friends');
        $(storage).on('friends_ready', () => {
            this.setState({
                friends: storage.data.friends,
                isLoading: false
            });
        });

        storage.getData('requests');
        $(storage).on('requests_ready', () => {
            console.log(storage);
            this.setState({
                requests: storage.data.requests
            });
        });
    }

}

export default FriendList;