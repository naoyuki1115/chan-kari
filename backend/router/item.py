import usecase.item
from database.database import get_db
from fastapi import APIRouter, Depends, HTTPException
from schema.item import ItemListRequest, ItemResponse
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/items",
)


@router.get("", response_model=list[ItemResponse])
def list_item(
    req: ItemListRequest = Depends(), db: Session = Depends(get_db)
) -> list[ItemResponse]:
    if req.after is not None and req.before is not None:
        raise HTTPException(
            status_code=400, detail="Only either Before or After can be specified"
        )
    return usecase.item.get_list(
        db, bool(req.available), req.limit, req.after, req.before
    )
