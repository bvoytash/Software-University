import {page} from './lib.js';
import {render, html} from './lib.js';
import * as api from './data.js';
import { homePage } from './views/home.js';
import { catalogPage } from './views/catalog.js';
import { loginPage } from './views/login.js';
import {logout} from './data.js'
import { registerPage } from './views/register.js';
import {getUserData} from './api/util.js';
import { createPage } from './views/create.js';
import { detailsPage } from './views/details.js';
import { editPage } from './views/edit.js';
import { profilePage } from './views/profile.js';

window.api = api;

const root = document.querySelector('main');
document.getElementById('logoutBtn').addEventListener('click', onLogout);

page(decorateContext);
page('/', homePage);
page('/memes', catalogPage);
page('/login', loginPage);
page('/register', registerPage);
page('/create', createPage);
page('/details/:id', detailsPage);
page('/edit/:id', editPage);
page('/profile', profilePage);

updateNavigation();
page.start();


function decorateContext(ctx, next){
    ctx.render = (content) => render(content, root);
    ctx.updateNavigation = updateNavigation;
    next();
}

function updateNavigation(){
    const userData = getUserData();

    if(userData){
        document.querySelector('.user').style.display = 'block';
        document.querySelector('.guest').style.display = 'none';
        document.querySelector('.user span').textContent = `Welcome, ${userData.email}`;
    }else{
        document.querySelector('.user').style.display = 'none';
        document.querySelector('.guest').style.display = 'block';
    }
}

async function onLogout(){
    await logout();
    updateNavigation();
    page.redirect('/');
}