/**
 *  \file gtk_Bin.cpp
 */

#include "gtk_Bin.hpp"

#include "gtk_Widget.hpp"

#include <gtk/gtk.h>

/*#
   @beginmodule gtk
*/

namespace Falcon {
namespace Gtk {

/**
 *  \brief module init
 */
void Bin::modInit( Falcon::Module* mod )
{
    Falcon::Symbol* c_Bin = mod->addClass( "GtkBin", &Gtk::abstract_init );

    Falcon::InheritDef* in = new Falcon::InheritDef( mod->findGlobalSymbol( "GtkContainer" ) );
    c_Bin->getClassDef()->addInheritance( in );

    c_Bin->getClassDef()->factory( &Bin::factory );

    mod->addClassMethod( c_Bin, "get_child",    &Bin::get_child );

}


Bin::Bin( const Falcon::CoreClass* gen, const GtkBin* bin )
    :
    Gtk::CoreGObject( gen, (GObject*) bin )
{}


Falcon::CoreObject* Bin::factory( const Falcon::CoreClass* gen, void* bin, bool )
{
    return new Bin( gen, (GtkBin*) bin );
}


/*#
    @class GtkBin
    @brief The GtkBin widget is a container with just one child.

    It is not very useful itself, but it is useful for deriving subclasses,
    since it provides common code needed for handling a single child widget.
 */

/*#
    @method get_child GtkBin
    @brief Gets the child of the GtkBin, or Nil if the bin contains no child widget.
 */
FALCON_FUNC Bin::get_child( VMARG )
{
#ifndef NO_PARAMETER_CHECK
    if ( vm->paramCount() )
    {
        throw_require_no_args();
    }
#endif
    MYSELF;
    GET_OBJ( self );
    GtkWidget* gwdt = gtk_bin_get_child( (GtkBin*)_obj );
    if ( gwdt )
    {
        Item* wki = vm->findWKI( "GtkWidget" );
        vm->retval( new Gtk::Widget( wki->asClass(), gwdt ) );
    }
    else
        vm->retnil();
}


} // Gtk
} // Falcon

// vi: set ai et sw=4:
// kate: replace-tabs on; shift-width 4;