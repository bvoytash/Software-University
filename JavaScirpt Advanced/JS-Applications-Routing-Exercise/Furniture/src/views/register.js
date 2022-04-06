import { register } from '../data.js';
import { html } from '../lib.js';

const registerTemplate = (onSubmit) =>  html`
<form @submit=${onSubmit}>
    <div class="row space-top">
        <div class="col-md-4">
            <div class="form-group">
                <label class="form-control-label" for="email">Email</label>
                <input class="form-control" id="email" type="text" name="email">
            </div>
            <div class="form-group">
                <label class="form-control-label" for="password">Password</label>
                <input class="form-control" id="password" type="password" name="password">
            </div>
            <div class="form-group">
                <label class="form-control-label" for="rePass">Repeat</label>
                <input class="form-control" id="rePass" type="password" name="rePass">
            </div>
            <input type="submit" class="btn btn-primary" value="Register" />
        </div>
    </div>
</form>`;

export function registerPage(ctx){
    ctx.render(registerTemplate(onSubmit));
    console.log('asd');

    async function onSubmit(event){
        event.preventDefault();
        const formData = new FormData(event.target);

        const email = formData.get('email');
        const password = formData.get('password');
        const repass = formData.get('rePass');
        
        if(email == '' || password == ''){
            return alert('All fields are reqiured!')
        }
        if(password != repass){
            return alert('Pass do not match!')
        }
        await register(email , password);
        ctx.page.redirect('/');
        ctx.updateNavigation();
    }
}