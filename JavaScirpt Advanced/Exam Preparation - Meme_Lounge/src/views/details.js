import { getUserData } from '../api/util.js';
import { deleteItem, getById } from '../data.js';
import {html} from '../lib.js';

const detailsTemplate = (meme, isOwner, onDelete) => html`
 <section id="meme-details">
    <h1>Meme Title: ${meme.title}

    </h1>
    <div class="meme-details">
        <div class="meme-img">
            <img alt="meme-alt" src="${meme.imageUrl}">
        </div>
        <div class="meme-description">
            <h2>Meme Description</h2>
            <p>${meme.description}</p>

            ${isOwner ? html`<a class="button warning" href="/edit/${meme._id}">Edit</a>
            <button @click="${onDelete}" class="button danger">Delete</button>` : null}    
        </div>
    </div>
</section>`;

export async function detailsPage(ctx){
    const meme = await getById(ctx.params.id)
    const userData = getUserData();
    const isOwner = userData && userData.id == meme._ownerId;
    ctx.render(detailsTemplate(meme, isOwner, onDelete));

    async function onDelete(){
        const choice = confirm('Are you sure?');
        if(choice){
            await deleteItem(ctx.params.id);
            ctx.page.redirect('/memes');
        }
    }
}