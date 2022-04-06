import { logout } from './data.js';
import * as api from './data.js';
import {page} from './lib.js';
import {render, html} from './lib.js';
import { catalogPage } from './views/catalog.js';
import { homePage } from './views/home.js';
import { loginPage } from './views/login.js';
import { getUserData } from './api/util.js';
import { registerPage } from './views/register.js';
import {creatAlbum} from './views/create.js';
import { detailsAlbum } from './views/details.js';
import { editAlbum } from './views/edit.js';
import { searchPage } from './views/search.js';


window.api = api;

const root = document.getElementById('main-content');
document.getElementById('logoutBtn').addEventListener('click', onLogout);

page(decorateContext);
page('/catalog', catalogPage);
page('/', homePage);
page('/login', loginPage);
page('/register', registerPage);
page('/create', creatAlbum);
page('/details/:id', detailsAlbum);
page('/edit/:id', editAlbum);
page('/search', searchPage);

page.start();
updateNavigation();

function decorateContext(ctx, next){
    ctx.render = (content) => render(content, root);
    ctx.updateNavigation = updateNavigation;

    next();
}

async function onLogout(){
    await logout();
    updateNavigation();
    page.redirect('/');
}

export function updateNavigation(){
    const userData = getUserData();

    if(userData){
        document.getElementById('catalog').style.display = 'inline-block';
        document.getElementById('search').style.display = 'inline-block';
        document.getElementById('create').style.display = 'inline-block';
        document.getElementById('logoutBtn').style.display = 'inline-block';
        document.getElementById('login').style.display = 'none';
        document.getElementById('register').style.display = 'none';
    }else{
        document.getElementById('catalog').style.display = 'inline-block';
        document.getElementById('search').style.display = 'inline-block';
        document.getElementById('create').style.display = 'none';
        document.getElementById('logoutBtn').style.display = 'none';
        document.getElementById('login').style.display = 'inline-block';
        document.getElementById('register').style.display = 'inline-block';
    }
}