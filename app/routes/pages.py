from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(tags=["Pages"])

templates = Jinja2Templates(directory="templates")


@router.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="productos.html",
        context={}
    )

@router.get("/inventario")
def inventario(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="inventario.html",
        context={}
    )

@router.get("/ventas")
def ventas(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="ventas.html",
        context={}
    )

@router.get("/ventas")
def ventas(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="ventas.html",
        context={}
    )

@router.get("/kardex")
def kardex(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="kardex.html",
        context={}
    )