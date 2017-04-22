/**
 * Created by geoolekom on 13.04.17.
 */

import React from 'react';
import storage from '../Storage';
import $ from 'jquery';

class Feed extends React.Component {

    state = {
        users: [],
        posts: [],
        isLoading: true,
    };

    render() {
        return <div>
            { this.state.posts }
        </div>
    }

    componentDidMount = () => {
        storage.getData('posts');
        $(storage).on('posts_ready', () => {
            this.setState({
                posts: storage.data.posts
            });
        });
    }
}

export default Feed;
