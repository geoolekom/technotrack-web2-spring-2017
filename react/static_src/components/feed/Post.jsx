import React from 'react';
import {Panel, ListGroup, ListGroupItem} from 'react-bootstrap';

class Post extends React.Component {
    render() {
        return <Panel collapsible defaultExpanded header={ this.props.title }>
            { this.props.content }
            <ListGroup fill>
                <ListGroupItem>Рейтинг: { this.props.likes }</ListGroupItem>
                <ListGroupItem>Автор: { this.props.author.username }</ListGroupItem>
            </ListGroup>
        </Panel>;
    }
}

Post.propTypes = {
    author: React.PropTypes.shape({
        username: React.PropTypes.string.isRequired,
    }),
    title: React.PropTypes.string.isRequired,
    content: React.PropTypes.string.isRequired,
    likes: React.PropTypes.number.isRequired
};

export default Post;