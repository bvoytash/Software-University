import { logout, register } from './api/api.js';
import { getUserData } from './api/util.js';
import * as api from './data.js';
import {page} from './lib.js';
import {render, html} from './lib.js';
import { createBook } from './views/create.js';
import { dashbordPage } from './views/dashbord.js';
import { detailsBook } from './views/details.js';
import { editBook } from './views/edit.js';
import { loginPage } from './views/login.js';
import { myBooks } from './views/mybooks.js';
import { registerPage } from './views/register.js';

window.api = api;

const root = document.getElementById('site-content');
document.getElementById('logoutBtn').addEventListener('click', onLogout);

page(decorateContext);
page('/', dashbordPage);
page('/login', loginPage);
page('/register', registerPage);
page('/create', createBook);
page('/details/:id', detailsBook);
page('/mybooks', myBooks);
page('/edit/:id', editBook);


page.start();
updateNavigation();

function updateNavigation(){
    const userData = getUserData();

    if(userData){
        document.getElementById('user').style.display = 'block';
        document.getElementById('guest').style.display = 'none';
        document.querySelector('#user span').textContent = `Welcome, ${userData.email}`;
    }else{
        document.getElementById('user').style.display = 'none';
        document.getElementById('guest').style.display = 'block';
    }
}

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