import React from 'react';
import $ from 'jquery';
import Friend from "./Friend";
import { ListGroupItem, ListGroup } from "react-bootstrap";

const friends_url = 'http://socnet.local/api/v1/friendships.json';
const requests_url = 'http://socnet.local/api/v1/friendship_requests';
const users_url = 'http://socnet.local/api/v1/users';

class FriendList extends React.Component {

    state = {
        friendships: [],
        requests: [],
        isLoading: true
    };

    render() {
        if (this.state.isLoading) {
            return <div>Идет загрузка...</div>
        } else {
            return <ListGroup>
                { this.state.requests }
                { this.state.friendships }
            </ListGroup>
        }
    }

    componentDidMount() {
        let users = [];
        let friendships = [];

        $.ajax({
            method: 'get',
            url: users_url,
        }).done((response) => {
            users = response.reduce((dict, obj) => {
                dict[obj.id] = obj;
                return dict;
            }, {});

            $.ajax({
                method: 'get',
                url: friends_url,
            }).done((response) => {
                friendships = response.map(
                    elem => <Friend key={ elem.id } name={ users[elem.friend].username } status="friend" />
                );

                this.setState({
                    friendships: friendships,
                    isLoading: false
                });
            }).fail((response) => {
                console.log('Не удалось загрузить друзей: ', response);
            });

            let requests = [];

            $.ajax({
                method: 'get',
                url: requests_url,
            }).done((response) => {
                requests = response.reduce((arr, elem) => {
                    if (!elem.accepted) {
                        arr.push(<Friend key={ elem.id } name={ users[elem.target].username } status="incoming" />)
                    }
                    return arr
                }, []);

                this.setState({
                    requests: requests
                });

            }).fail((response) => {
                console.log('Не удалось загрузить запросы в друзья: ', response);
            });
        }).fail((response) => {
            console.log('Не удалось загрузить пользователей: ', response);
        });
    }

}

export default FriendList;