from fastapi import APIRouter

order_router=APIRouter(prefix='/orders',tags=['Orders'])

@order_router.get('/')
async def get_orders():
    return{"message":"This is From Orders"}
