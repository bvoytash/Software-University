import {page} from './lib.js';
import{render} from './lib.js';
import {catalogPage} from './views/catalog.js';
import {detailPage} from './views/details.js';
import {createPage} from './views/create.js';
import {loginPage} from './views/login.js';
import {registerPage} from './views/register.js';
import {editPage} from './views/edit.js';
import * as api from './data.js'
import { logout } from './api/api.js';
import { getUserData } from './api/util.js';

window.api = api;

const root = document.querySelector('div.container');
document.getElementById('logoutBtn').addEventListener('click', onLogout);

page(decorateContext);
page('/', catalogPage);
page('/details/:id', detailPage);
page('/create', createPage);
page('/login', loginPage);
page('/register', registerPage);
page('/my-furniture', catalogPage);
page('/edit/:id', editPage);
    
page.start();
updateNavigation()

export function updateNavigation(){
    const userData = getUserData();
    if(userData){
        document.getElementById('user').style.display = 'inline-block';
        document.getElementById('guest').style.display = 'none';
    }else{
        document.getElementById('user').style.display = 'none';
        document.getElementById('guest').style.display = 'inline-block';
    }
}

function decorateContext(ctx, next){
    ctx.render = (content) => render(content, root);
    ctx.updateNavigation = updateNavigation;
    next();
}

async function onLogout(){
    await logout();
    page.redirect('/');
    updateNavigation();
}