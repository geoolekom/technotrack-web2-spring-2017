import $ from 'jquery';
import React from 'react';
import Post from "./feed/Post";

const requirements = {
    users: [],
    posts: ['users'],
    friends: ['users'],
    requests: ['users'],
};

const handlers = {
    users: elem => ({
        username: elem.username,
        key: elem.id,
    }),
    posts: elem => (
        <Post key={ elem.id } author={ storage['users'].find(x => x.key === elem.author) } title={ elem.title } content={ elem.content } likes={ elem.like_count } />
    )
};

function api_request(entity, callback, method='get') {
    let url = 'http://socnet.local/api/v1/' + entity + '.json';
    $.ajax({
        method: method,
        url: url,
        user: 'geoolekom',
        password: 'qwerty123'
    }).done((response) => {
        callback(response)
    }).fail((response) => {
        console.log('Не удалось загрузить: ', response);
    });
}

class Storage {

    data = {
        users: [],
        posts: [],
        friends: [],
        requests: []
    };
    handlers = {
        users: elem => ({
            username: elem.username,
            key: elem.id,
        }),
        posts: elem => (
            <Post key={ elem.id } author={ this.data.users.find(x => x.key === elem.author) } title={ elem.title } content={ elem.content } likes={ elem.like_count } />
        )
    };
    requirements = {
        users: [],
        posts: ['users'],
        friends: ['users'],
        requests: ['users'],
    };

    constructor() {
        let storage = this;
        $(storage).on('required', (event, entity, response) => {
            if (storage.requirements[entity].length) {
                let left = storage.requirements[entity].slice();
                $(storage.requirements[entity]).each(
                    (index, r) => {
                        $(storage).on(r + '_ready', () => {
                            left.splice(left.indexOf(r), 1);
                            if (left.length === 0) {
                                storage.data[entity] = response.map(storage.handlers[entity]);
                                $(storage).trigger(entity + '_ready');
                            }
                        });
                        storage.getData(r);
                    }
                );

                let a = () => {
                    console.log(entity);
                    $(storage).trigger('satisfied', [entity, response]);
                }
            } else {
                storage.data[entity] = response.map(storage.handlers[entity]);
                $(storage).trigger(entity + '_ready');
            }
        });
    };
    getData = (entity) => {
        let storage = this;
        if (storage.data[entity].length > 0) {
            $(storage).trigger(entity + '_ready');
        } else {
            api_request(entity, function (response) {
                $(storage).trigger('required', [entity, response]);
            });
        }
    };
}

let storage = new Storage();

export default storage;